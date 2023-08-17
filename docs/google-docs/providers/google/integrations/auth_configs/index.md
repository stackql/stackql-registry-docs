---
title: auth_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - auth_configs
  - integrations
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auth_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.integrations.auth_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the SFDC instance projects/&#123;project&#125;/locations/&#123;location&#125;/authConfigs/&#123;authConfig&#125;. |
| `description` | `string` | A description of the auth config. |
| `encryptedCredential` | `string` | Auth credential encrypted by Cloud KMS. Can be decrypted as Credential with proper KMS key. |
| `creatorEmail` | `string` | The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call. |
| `decryptedCredential` | `object` | Defines parameters for a single, canonical credential. |
| `expiryNotificationDuration` | `array` | User can define the time to receive notification after which the auth config becomes invalid. Support up to 30 days. Support granularity in hours. |
| `reason` | `string` | The reason / details of the current status. |
| `createTime` | `string` | Output only. The timestamp when the auth config is created. |
| `lastModifierEmail` | `string` | The last modifier's email address. Generated based on the End User Credentials/LOAS role of the user making the call. |
| `overrideValidTime` | `string` | User provided expiry time to override. For the example of Salesforce, username/password credentials can be valid for 6 months depending on the instance settings. |
| `credentialType` | `string` | Credential type of the encrypted credential. |
| `displayName` | `string` | Required. The name of the auth config. |
| `visibility` | `string` | The visibility of the auth config. |
| `certificateId` | `string` | Certificate id for client certificate |
| `state` | `string` | The status of the auth config. |
| `updateTime` | `string` | Output only. The timestamp when the auth config is modified. |
| `validTime` | `string` | The time until the auth config is valid. Empty or max value is considered the auth config won't expire. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_auth_configs_get` | `SELECT` | `authConfigsId, locationsId, projectsId` | Gets a complete auth config. If the auth config doesn't exist, Code.NOT_FOUND exception will be thrown. Returns the decrypted auth config. |
| `projects_locations_auth_configs_list` | `SELECT` | `locationsId, projectsId` | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| `projects_locations_products_auth_configs_get` | `SELECT` | `authConfigsId, locationsId, productsId, projectsId` | Gets a complete auth config. If the auth config doesn't exist, Code.NOT_FOUND exception will be thrown. Returns the decrypted auth config. |
| `projects_locations_products_auth_configs_list` | `SELECT` | `locationsId, productsId, projectsId` | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| `projects_locations_auth_configs_create` | `INSERT` | `locationsId, projectsId` | Creates an auth config record. Fetch corresponding credentials for specific auth types, e.g. access token for OAuth 2.0, JWT token for JWT. Encrypt the auth config with Cloud KMS and store the encrypted credentials in Spanner. Returns the encrypted auth config. |
| `projects_locations_products_auth_configs_create` | `INSERT` | `locationsId, productsId, projectsId` | Creates an auth config record. Fetch corresponding credentials for specific auth types, e.g. access token for OAuth 2.0, JWT token for JWT. Encrypt the auth config with Cloud KMS and store the encrypted credentials in Spanner. Returns the encrypted auth config. |
| `projects_locations_auth_configs_delete` | `DELETE` | `authConfigsId, locationsId, projectsId` | Deletes an auth config. |
| `projects_locations_products_auth_configs_delete` | `DELETE` | `authConfigsId, locationsId, productsId, projectsId` | Deletes an auth config. |
| `_projects_locations_auth_configs_list` | `EXEC` | `locationsId, projectsId` | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| `_projects_locations_products_auth_configs_list` | `EXEC` | `locationsId, productsId, projectsId` | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| `projects_locations_auth_configs_patch` | `EXEC` | `authConfigsId, locationsId, projectsId` | Updates an auth config. If credential is updated, fetch the encrypted auth config from Spanner, decrypt with Cloud KMS key, update the credential fields, re-encrypt with Cloud KMS key and update the Spanner record. For other fields, directly update the Spanner record. Returns the encrypted auth config. |
| `projects_locations_products_auth_configs_patch` | `EXEC` | `authConfigsId, locationsId, productsId, projectsId` | Updates an auth config. If credential is updated, fetch the encrypted auth config from Spanner, decrypt with Cloud KMS key, update the credential fields, re-encrypt with Cloud KMS key and update the Spanner record. For other fields, directly update the Spanner record. Returns the encrypted auth config. |
