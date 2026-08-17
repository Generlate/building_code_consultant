use std::env;
use std::io::{self, Write};

use dotenvy::dotenv;
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // load .env
    dotenv().ok();
    let openai_api_key = env::var("OPENAI_API_KEY")
        .expect("OPENAI_API_KEY must be set in the environment or .env file");

    // use this on the .json data to format it. (terminal)
    // openai tools fine_tunes.prepare_data -f ./datasets/municode_florida_west_palm_beach_chapter94_zoning_and_land_development_regulations.json

    // authorize the api with the key from https://platform.openai.com/account/api-keys
    // (key is read into `openai_api_key` above and sent as a bearer token below)

    // create a fine tune model. (terminal)
    // openai api fine_tunes.create -t ./datasets/municode_florida_west_palm_beach_chapter94_zoning_and_land_development_regulations.json -m davinci

    // Enter a prompt and get an answer (called a completion).
    print!("Enter your prompt: ");
    io::stdout().flush()?;
    let mut prompt = String::new();
    io::stdin().read_line(&mut prompt)?;
    let prompt = prompt.trim();

    let client = reqwest::Client::new();
    let response = client
        .post("https://api.openai.com/v1/completions")
        .bearer_auth(&openai_api_key)
        .json(&json!({
            "model": "davinci:ft-personal-2023-07-14-10-54-52",
            "prompt": prompt
        }))
        .send()
        .await?;

    let body: serde_json::Value = response.json().await?;
    println!("{}", serde_json::to_string_pretty(&body)?);

    Ok(())
}

// TODO: move all Rust code to a different place and run `cargo new` to create a new Rust project. Then do a 'hello world'. Then delete and move the code into the generated files. 