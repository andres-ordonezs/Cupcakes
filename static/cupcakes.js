"use strict";

const $form = $("#newCupcakeForm");



async function handleFormSubmit(evt) {
  evt.preventDefault();

  const data = {
    flavor: $("#flavor").val(),
    size: $("#size").val(),
    rating: $("#rating").val(),
    image_url: $("#image_url").val()
  };

  const response = await fetch(`/api/cupcakes`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "content-type": "application/json",
    }
  });

  const cupcake = await response.json();

  console.log(cupcake);

}

$form.on("submit", handleFormSubmit);