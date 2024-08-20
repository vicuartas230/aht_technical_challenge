const deleteItem = (id) => {
    $.ajax({
        type: "DELETE",
        url: `/delete/${id}`,
        success: function (response) {
            window.location.reload();
        }
    });
};
