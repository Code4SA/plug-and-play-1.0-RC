﻿/**
 * @license Copyright (c) CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

(function() {
    if (!supportsLocalStorage()) {
        return;
    }


   
    CKEDITOR.plugins.add("autosave", {
        lang: ['de', 'en', 'es'],
        init: function (editor) {
            
			editor.lang.autosave = ''
            // Checks If there is data available and load it
            if (localStorage.getItem('autosave' + editor.id)) {

                var autoSavedContent = localStorage.getItem('autosave' + editor.id);
                var editorLoadedContent = editor.getData();
                
                // check if the loaded editor content is the same as the autosaved content
                if (editorLoadedContent == autoSavedContent) {

                    localStorage.removeItem('autosave' + editor.id);

                    return;
                }

                if (confirm("Hay Texto en el Borrador, desea recuperarlo?")) {

                    editor.setData(localStorage.getItem('autosave' + editor.id));
                }

                localStorage.removeItem('autosave' + editor.id);
            }

            editor.on('key', startTimer);
        }
    });

    var timeOutId = 0,
        savingActive = false;

    var startTimer = function(event) {
        if (timeOutId) {
            clearTimeout(timeOutId);
        }
        var delay = CKEDITOR.config.autosave_delay != null ? CKEDITOR.config.autosave_delay : 10;
        timeOutId = setTimeout(onTimer, delay * 1000, event);
    };
    var onTimer = function(event) {
        if (savingActive) {
            startTimer(event);
        } else if (event.editor.checkDirty()) {
            savingActive = true;

            // save content
            localStorage.setItem('autosave' + event.editor.id, event.editor.getData());

            //alert("Auto-Saved");

            savingActive = false;
        }
    };

    // localStorage detection
    function supportsLocalStorage() {
        return typeof(Storage) !== 'undefined';
    }

	
})();