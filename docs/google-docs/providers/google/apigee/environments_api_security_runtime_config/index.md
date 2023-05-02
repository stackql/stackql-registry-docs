---
title: environments_api_security_runtime_config
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_api_security_runtime_config
  - apigee
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
<tr><td><b>Name</b></td><td><code>environments_api_security_runtime_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.environments_api_security_runtime_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the environment API Security Runtime configuration resource. Format: `organizations/&#123;org&#125;/environments/&#123;env&#125;/apiSecurityRuntimeConfig` |
| `revisionId` | `string` | Revision ID of the API Security Runtime configuration. The higher the value, the more recently the configuration was deployed. |
| `uid` | `string` | Unique ID for the API Security Runtime configuration. The ID will only change if the environment is deleted and recreated. |
| `updateTime` | `string` | Time that the API Security Runtime configuration was updated. |
| `location` | `array` | A list of up to 5 Cloud Storage Blobs that contain SecurityActions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_environments_getApiSecurityRuntimeConfig` | `SELECT` | `environmentsId, organizationsId` |
