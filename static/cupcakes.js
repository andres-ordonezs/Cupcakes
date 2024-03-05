"use strict";
//Initialize form element.
const $form = $("#newCupcakeForm");


/**
 * Sets form data and handles form submit.
 *
 */
async function handleFormSubmit(evt) {
  evt.preventDefault();

  const cupcakeData = {
    flavor: $("#flavor").val(),
    size: $("#size").val(),
    rating: $("#rating").val(),
    image_url: $("#image_url").val()
  };

  const cupcake = await make_new_cupcake_post(cupcakeData);
  console.log(cupcake);
  appendCupcake(cupcake.cupcake);

}

/**
 * make_new_cupcake_post: Takes cupcakeData from form and makes post request to
 * api to create a new cupcake. Returns the new cupcake response from api.
 *
 */
async function make_new_cupcake_post(cupcakeData) {

  const response = await fetch(`/api/cupcakes`, {
    method: "POST",
    body: JSON.stringify(cupcakeData),
    headers: {
      "content-type": "application/json",
    }
  });

  const cupcake = await response.json();

  return (cupcake);

}

/**
 *appendCupcake: Takes new cupcake data and appends to the page.
 */
function appendCupcake(cupcake) {
  const $cupcake = $(`<div>
                        <img src=${cupcake.image_url}>
                        <h1>${cupcake.flavor}</h1>
                        <li>Size: ${cupcake.size}</li>
                        <li>Rating: ${cupcake.rating}</li>
                      </div>`);


  $("#cupcakeList").append($cupcake);

}


$form.on("submit", handleFormSubmit);