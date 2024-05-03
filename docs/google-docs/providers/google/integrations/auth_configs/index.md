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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auth_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.auth_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the SFDC instance projects/&#123;project&#125;/locations/&#123;location&#125;/authConfigs/&#123;authConfig&#125;. |
| <CopyableCode code="description" /> | `string` | A description of the auth config. |
| <CopyableCode code="certificateId" /> | `string` | Certificate id for client certificate |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the auth config is created. |
| <CopyableCode code="creatorEmail" /> | `string` | The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call. |
| <CopyableCode code="credentialType" /> | `string` | Credential type of the encrypted credential. |
| <CopyableCode code="decryptedCredential" /> | `object` | Defines parameters for a single, canonical credential. |
| <CopyableCode code="displayName" /> | `string` | Required. The name of the auth config. |
| <CopyableCode code="encryptedCredential" /> | `string` | Auth credential encrypted by Cloud KMS. Can be decrypted as Credential with proper KMS key. |
| <CopyableCode code="expiryNotificationDuration" /> | `array` | User can define the time to receive notification after which the auth config becomes invalid. Support up to 30 days. Support granularity in hours. |
| <CopyableCode code="lastModifierEmail" /> | `string` | The last modifier's email address. Generated based on the End User Credentials/LOAS role of the user making the call. |
| <CopyableCode code="overrideValidTime" /> | `string` | User provided expiry time to override. For the example of Salesforce, username/password credentials can be valid for 6 months depending on the instance settings. |
| <CopyableCode code="reason" /> | `string` | The reason / details of the current status. |
| <CopyableCode code="state" /> | `string` | The status of the auth config. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the auth config is modified. |
| <CopyableCode code="validTime" /> | `string` | The time until the auth config is valid. Empty or max value is considered the auth config won't expire. |
| <CopyableCode code="visibility" /> | `string` | The visibility of the auth config. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_auth_configs_get" /> | `SELECT` | <CopyableCode code="authConfigsId, locationsId, projectsId" /> | Gets a complete auth config. If the auth config doesn't exist, Code.NOT_FOUND exception will be thrown. Returns the decrypted auth config. |
| <CopyableCode code="projects_locations_auth_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| <CopyableCode code="projects_locations_products_auth_configs_get" /> | `SELECT` | <CopyableCode code="authConfigsId, locationsId, productsId, projectsId" /> | Gets a complete auth config. If the auth config doesn't exist, Code.NOT_FOUND exception will be thrown. Returns the decrypted auth config. |
| <CopyableCode code="projects_locations_products_auth_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| <CopyableCode code="projects_locations_auth_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an auth config record. Fetch corresponding credentials for specific auth types, e.g. access token for OAuth 2.0, JWT token for JWT. Encrypt the auth config with Cloud KMS and store the encrypted credentials in Spanner. Returns the encrypted auth config. |
| <CopyableCode code="projects_locations_products_auth_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Creates an auth config record. Fetch corresponding credentials for specific auth types, e.g. access token for OAuth 2.0, JWT token for JWT. Encrypt the auth config with Cloud KMS and store the encrypted credentials in Spanner. Returns the encrypted auth config. |
| <CopyableCode code="projects_locations_auth_configs_delete" /> | `DELETE` | <CopyableCode code="authConfigsId, locationsId, projectsId" /> | Deletes an auth config. |
| <CopyableCode code="projects_locations_products_auth_configs_delete" /> | `DELETE` | <CopyableCode code="authConfigsId, locationsId, productsId, projectsId" /> | Deletes an auth config. |
| <CopyableCode code="_projects_locations_auth_configs_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| <CopyableCode code="_projects_locations_products_auth_configs_list" /> | `EXEC` | <CopyableCode code="locationsId, productsId, projectsId" /> | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| <CopyableCode code="projects_locations_auth_configs_patch" /> | `EXEC` | <CopyableCode code="authConfigsId, locationsId, projectsId" /> | Updates an auth config. If credential is updated, fetch the encrypted auth config from Spanner, decrypt with Cloud KMS key, update the credential fields, re-encrypt with Cloud KMS key and update the Spanner record. For other fields, directly update the Spanner record. Returns the encrypted auth config. |
| <CopyableCode code="projects_locations_products_auth_configs_patch" /> | `EXEC` | <CopyableCode code="authConfigsId, locationsId, productsId, projectsId" /> | Updates an auth config. If credential is updated, fetch the encrypted auth config from Spanner, decrypt with Cloud KMS key, update the credential fields, re-encrypt with Cloud KMS key and update the Spanner record. For other fields, directly update the Spanner record. Returns the encrypted auth config. |
