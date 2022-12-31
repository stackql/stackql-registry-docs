---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - firebaseappcheck
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebaseappcheck.apps</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_apps_exchangeAppAttestAssertion` | `EXEC` | `appsId:exchangeAppAttestAssertion, projectsId` | Accepts an App Attest assertion and an artifact previously obtained from ExchangeAppAttestAttestation and verifies those with Apple. If valid, returns an AppCheckToken. |
| `projects_apps_exchangeAppAttestAttestation` | `EXEC` | `appsId:exchangeAppAttestAttestation, projectsId` | Accepts an App Attest CBOR attestation and verifies it with Apple using your preconfigured team and bundle IDs. If valid, returns an attestation artifact that can later be exchanged for an AppCheckToken using ExchangeAppAttestAssertion. For convenience and performance, this method's response object will also contain an AppCheckToken (if the verification is successful). |
| `projects_apps_exchangeCustomToken` | `EXEC` | `appsId:exchangeCustomToken, projectsId` | Validates a custom token signed using your project's Admin SDK service account credentials. If valid, returns an AppCheckToken. |
| `projects_apps_exchangeDebugToken` | `EXEC` | `appsId:exchangeDebugToken, projectsId` | Validates a debug token secret that you have previously created using CreateDebugToken. If valid, returns an AppCheckToken. Note that a restrictive quota is enforced on this method to prevent accidental exposure of the app to abuse. |
| `projects_apps_exchangeDeviceCheckToken` | `EXEC` | `appsId:exchangeDeviceCheckToken, projectsId` | Accepts a [`device_token`](https://developer.apple.com/documentation/devicecheck/dcdevice) issued by DeviceCheck, and attempts to validate it with Apple. If valid, returns an AppCheckToken. |
| `projects_apps_exchangePlayIntegrityToken` | `EXEC` | `appsId:exchangePlayIntegrityToken, projectsId` | Validates an [integrity verdict response token from Play Integrity](https://developer.android.com/google/play/integrity/verdict#decrypt-verify). If valid, returns an AppCheckToken. |
| `projects_apps_exchangeRecaptchaEnterpriseToken` | `EXEC` | `appsId:exchangeRecaptchaEnterpriseToken, projectsId` | Validates a [reCAPTCHA Enterprise response token](https://cloud.google.com/recaptcha-enterprise/docs/create-assessment#retrieve_token). If valid, returns an AppCheckToken. |
| `projects_apps_exchangeRecaptchaV3Token` | `EXEC` | `appsId:exchangeRecaptchaV3Token, projectsId` | Validates a [reCAPTCHA v3 response token](https://developers.google.com/recaptcha/docs/v3). If valid, returns an AppCheckToken. |
| `projects_apps_exchangeSafetyNetToken` | `EXEC` | `appsId:exchangeSafetyNetToken, projectsId` | Validates a [SafetyNet token](https://developer.android.com/training/safetynet/attestation#request-attestation-step). If valid, returns an AppCheckToken. |
| `projects_apps_generateAppAttestChallenge` | `EXEC` | `appsId:generateAppAttestChallenge, projectsId` | Generates a challenge that protects the integrity of an immediately following call to ExchangeAppAttestAttestation or ExchangeAppAttestAssertion. A challenge should not be reused for multiple calls. |
| `projects_apps_generatePlayIntegrityChallenge` | `EXEC` | `appsId:generatePlayIntegrityChallenge, projectsId` | Generates a challenge that protects the integrity of an immediately following integrity verdict request to the Play Integrity API. The next call to ExchangePlayIntegrityToken using the resulting integrity token will verify the presence and validity of the challenge. A challenge should not be reused for multiple calls. |
