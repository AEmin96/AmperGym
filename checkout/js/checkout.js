// This is your test publishable API key.
const stripe = Stripe("pk_live_51OeDfNHcbPs5lobJhCwdNKUUs7IeLUtqkJuKx8Na81dRQQSFXrMeHTUcdppoYvaXsBcti7v4NwBCTSWqAaudNXAb00J41vX203");

initialize();

// Create a Checkout Session as soon as the page loads
async function initialize() {
  const response = await fetch("/create-checkout-session", {
    method: "POST",
  });

  const { clientSecret } = await response.json();

  const checkout = await stripe.initEmbeddedCheckout({
    clientSecret,
  });

  // Mount Checkout
  checkout.mount('#checkout');
}