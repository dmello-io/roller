var socket = io();

socket.on('connect', function () {
});

function disableInput(noRooms) {
    $("button").attr("disabled", "disabled");
    setTimeout(function () {
        $("button").removeAttr("disabled");
    }, 7000 * noRooms);
}

function getRooms(){
    var rooms = $(".custom-select").val();
    var strRooms = rooms.join(" ");
    return strRooms; 
}

function countRooms(){
    var sel = $('.custom-select').val();
    var count = sel.length;;
    return count;
}

$( ".custom-select" ).change(function() {
    var $select = $('select[class="custom-select"]'),
        $all = $select.find('option[value="room_all"]'),
        $opts = $select.find('option').not($all)
        $select.change(function () {
            if ($all.is(':selected')) {
                $opts.prop('selected', false);
            } else {
                $all.prop('selected', false);
            }
        });
  });

$(document).ready(function () {
    $(".btn-open").click(function () {
        var strRooms = getRooms();
        var noRooms = countRooms();
        disableInput(noRooms)
        socket.emit('open', strRooms);
    });
});

$(document).ready(function () {
    $(".btn-close").click(function () {
        var strRooms = getRooms();
        var noRooms = countRooms();
        disableInput(noRooms)
        socket.emit('close', strRooms);
    });
});

$(document).ready(function () {
    $(".btn-up").click(function () {
        socket.emit('virtual', 'button_up');
    });
});

$(document).ready(function () {
    $(".btn-pause").click(function () {
        socket.emit('virtual', 'button_pause');
    });
});

$(document).ready(function () {
    $(".btn-down").click(function () {
        socket.emit('virtual', 'button_down');
    });
});

$(document).ready(function () {
    $(".btn-prev").click(function () {
        socket.emit('virtual', 'button_prev');
    });
});

$(document).ready(function () {
    $(".btn-next").click(function () {
        socket.emit('virtual', 'button_next');
    });
});