 //sidenav
 $(document).ready(function () {
     $(".sidenav").sidenav();
     $('.slider').slider();
     $('.collapsible').collapsible();
     $('select').formSelect();
     $('.modal').modal({
         dismissible: false
     });
     $('.datepicker').datepicker({
         format: "dd mmmm, yyyy",
         minDate: new Date(),
         autoClose: true,
         showClearBtn: true,
         i18n: {
             done: "Select"
         }
     });
     $('.timepicker').timepicker({
         autoClose: true,
         twelveHour: false,
         showClearBtn: true,
         i18n: {
             cancel: "Cancel",
             clear: "Clear",
             done: "Select"
         }
     });

     validateMaterializeSelect();

     function validateMaterializeSelect() {
         let classValid = {
             "border-bottom": "1px solid #4caf50",
             "box-shadow": "0 1px 0 0 #4caf50"
         };
         let classInvalid = {
             "border-bottom": "1px solid #f44336",
             "box-shadow": "0 1px 0 0 #f44336"
         };
         if ($("select.validate").prop("required")) {
             $("select.validate").css({
                 "display": "block",
                 "height": "0",
                 "padding": "0",
                 "width": "0",
                 "position": "absolute"
             });
         }
         $(".select-wrapper input.select-dropdown").on("focusin", function () {
             $(this).parent(".select-wrapper").on("change", function () {
                 if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                     $(this).children("input").css(classValid);
                 }
             });
         }).on("click", function () {
             if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                 $(this).parent(".select-wrapper").children("input").css(classValid);
             } else {
                 $(".select-wrapper input.select-dropdown").on("focusout", function () {
                     if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                         if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                             $(this).parent(".select-wrapper").children("input").css(classInvalid);
                         }
                     }
                 });
             }
         });
     }

     $('.fixed-action-btn').floatingActionButton();

     let counter1 = 1;

     function duplicate() {
         $("#card_c").after(`<div id="card_c${counter1}" class="row">
                    <div class="card-panel col s12 m6 offset-m3">
                        <div class="first_itinerary_card">
                            <div class="row">
                                <div class="input-field col s6 col s10 offset-m1 offset-m1">
                                    <i class="fas fa-pencil-alt prefix light-blue-text text-accent-2"></i>
                                    < input id = "activity_name"
                                    name = "activity_name"
                                    minlength = "5"
                                    maxlength = "50"
                                        type="text" class="validate" required>
                                    <label for="activity_name">Activity Name</label>
                                </div>
                            </div>
                            <!-- day -->
                            <div class="input-field col s3 offset-m1">
                                <i class="fas fa-calendar-day prefix light-blue-text text-accent-2"></i>
                                < input id = "day"
                                name = "day"
                                type = "number"
                                min = "1"
                                class = "validate"
                                required >
                                <label for="day">Day</label>
                            </div>
                            <!-- timepicker -->
                            <div class="input-field col s3">
                                <i class="fas fa-clock prefix light-blue-text text-accent-2"></i>
                                < input id = "time"
                                name = "time"
                                type = "text"
                                class = "timepicker validate"
                                required >
                                <label for="time">Time</label>
                            </div>
                            <!-- duration of itinerary item -->
                            <div class="input-field col s3">
                                <i class="fas fa-stopwatch prefix light-blue-text text-accent-2"></i>
                                < input id = "duration"
                                name = "duration"
                                type = "number"
                                step = "10"
                                min = "0"
                                class = "validate"
                                    required>
                                <label for="duration">Duration(Minutes)</label>
                            </div>
                            <!-- itinerary item description -->
                            <div class="row">
                                <div class="input-field col s10 offset-m1 offset-m1">
                                    <i class="fas fa-align-left prefix light-blue-text text-accent-2"></i>
                                    < textarea id = "item_description"
                                    name = "item_description"
                                    minlength = "5"
                                        maxlength="200" class="materialize-textarea validate" required></textarea>
                                    <label for="item_description">Description</label>
                                    <a class="btn-floating red btn-large right waves-effect waves-light red activator"
                                        onclick="duplicate();"><i class="fas fa-plus"></i></a>
                                        < a class = "btn-floating btn-large left waves-effect waves-light dark-blue activator"
                                         onclick = "duplicate();" > < i class = "fas fa-minus" > < /i></a >
                                </div>
                            </div>
                        </div>
                    </div>
                </div>`);
         counter1++;

     }

     $(".btn-floating.red").click(duplicate);
 });

 let counter1 = 1;

 function duplicate() {
     $("#card_c").after(`<div id="card_c${counter1}" class="row">
                    <div class="card-panel col s12 m6 offset-m3">
                        <div class="first_itinerary_card">
                            <div class="row">
                                <div class="input-field col s6 col s10 offset-m1 offset-m1">
                                    <i class="fas fa-pencil-alt prefix light-blue-text text-accent-2"></i>
                                    < input id = "activity_name"
                                    name = "activity_name"
                                    minlength = "5"
                                    maxlength = "50"
                                        type="text" class="validate" required>
                                    <label for="activity_name">Activity Name</label>
                                </div>
                            </div>
                            <!-- day -->
                            <div class="input-field col s3 offset-m1">
                                <i class="fas fa-calendar-day prefix light-blue-text text-accent-2"></i>
                                < input id = "day"
                                name = "day"
                                type = "number"
                                min = "1"
                                class = "validate"
                                required >
                                <label for="day">Day</label>
                            </div>
                            <!-- timepicker -->
                            <div class="input-field col s3">
                                <i class="fas fa-clock prefix light-blue-text text-accent-2"></i>
                                < input id = "time"
                                name = "time"
                                type = "text"
                                class = "timepicker validate"
                                required >
                                <label for="time">Time</label>
                            </div>
                            <!-- duration of itinerary item -->
                            <div class="input-field col s3">
                                <i class="fas fa-stopwatch prefix light-blue-text text-accent-2"></i>
                                < input id = "duration"
                                name = "duration"
                                type = "number"
                                step = "10"
                                min = "0"
                                class = "validate"
                                    required>
                                <label for="duration">Duration(Minutes)</label>
                            </div>
                            <!-- itinerary item description -->
                            <div class="row">
                                <div class="input-field col s10 offset-m1 offset-m1">
                                    <i class="fas fa-align-left prefix light-blue-text text-accent-2"></i>
                                    < textarea id = "item_description"
                                    name = "item_description"
                                    minlength = "5"
                                        maxlength="200" class="materialize-textarea validate" required></textarea>
                                    <label for="item_description">Description</label>
                                    <a class="btn-floating red btn-large right waves-effect waves-light red activator"
                                        onclick="duplicate();"><i class="fas fa-plus"></i></a>
                                        < a class = "btn-floating btn-large left waves-effect waves-light dark-blue activator"
                                         onclick = "duplicate();" > < i class = "fas fa-minus" > < /i></a >
                                </div>
                            </div>
                        </div>
                    </div>
                </div>`);
     counter1++;

 }