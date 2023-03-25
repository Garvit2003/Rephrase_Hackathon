import os

import requests

bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhNcHdjdFl4YWlRdWg4Y0M0ejN0UCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucmVwaHJhc2UuYWkvIiwic3ViIjoiYXV0aDB8NjQxZTk4YjEwMTZhMGQ0OWY5ODVlNWYwIiwiYXVkIjpbImh0dHBzOi8vZGl5LnJlcGhyYXNlLmFpL2F1dGgwIiwiaHR0cHM6Ly9yZXBocmFzZWFpLXByb2QudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3OTc0NzQwMCwiZXhwIjoxNjc5ODMzODAwLCJhenAiOiIzS1U1anZFcVdKQkNVS25QWDI2b25hU1B5M2pKMzBKNCIsInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUgcmVhZDpyZXBocmFzZS5haSBhbGw6ZGl5IHJlYWQ6cmVwaHJhc2UuYWkifQ.EvGLHwITlkK3aLQ3FQ2t7LejPIsbQcnk7QJoh9RzsdXoQWlGz6yQ0ZNko04xPiH6Hmp053RpZNupzqqWJIPu-lFJEQoRY1bt4IXnr4o0SKOTPJPg4weDaEP73bK50z_NT1Mjm5U8hz6NUPG1Wpdte3lkJMVqc37mFs9icMGlwuyIEn4nkVo__lSmwj_-rOTdb7n4r5t-zVNMjl0AN2-BMVVWUHHW15yRU_sqAPug72CfBg_LCqJsiZwJs1PuHVM0q7ceP2Pbfo0BMgWGOOWg-OAc53o2zskOyiIZFbzxG68kWFlq-XauIWWFiSOIgKb_bmuj-kCwXxCSl75gOf6nZA"

url = "https://personalized-brand.api.rephrase.ai/v2/campaign/create"

# open text file in read mode
text_file = open("E:\Code\Rephrase SDE hackathon\Resume.txt", "r")

# read whole file to a string
data = text_file.read()

# close file
text_file.close()

# read_file = print(data)

payload = {
    "videoDimension": {"height": 1080, "width": 1920},
    "scenes": [
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://www.musicinminnesota.com/wp-content/uploads/2021/02/Michael-Jackson-live.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "kind": "Spokesperson",
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": f"<speak>{{data}}</speak>",
                            "transcript_type": "text",
                        },
                    },
                },
            ]
        },

    ],
    # "title": "Into to MJ",
    # "thumbnailUrl": "https://blog.siriusxm.com/wp-content/uploads/2022/11/MichaelJacksonChannel-1117.jpg",
}

# {
#     "key": "https://stablediffusionapi.com/api/v3/text2img",
#     "prompt": "ultra realistic ",
#     "negative_prompt": "((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, (((skinny))), glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs)), anime",
#     "width": "512",
#     "height": "512",
#     "samples": "1",
#     "num_inference_steps": "20",
#     "safety_checker": "no",
#     "enhance_prompt": "yes",
#     "seed": null,
#     "guidance_scale": 7.5,
#     "webhook": null,
#     "track_id": null
# }

headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
    "content-type": "application/json",
}


response = requests.post(url, json=payload, headers=headers)

print(f"CAMPAIGN_ID= {response.text}")
