 //sidenav
 $(document).ready(function () {
     $(".sidenav").sidenav();
     $('.slider').slider();
     $('.collapsible').collapsible();
     $('select').formSelect();
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
     $('.fixed-action-btn').floatingActionButton();
     $('#itinerary_card.first_itinerary_card').click(function () {
         $('#itinerary_card.first_itinerary_card').clone().find('row').val('').end.
         find('textarea').val('').end.appendTo('#itinerary_card_new.card-panel');
     });
 });