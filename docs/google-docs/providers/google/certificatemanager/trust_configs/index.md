---
title: trust_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_configs
  - certificatemanager
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
<tr><td><b>Name</b></td><td><code>trust_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.certificatemanager.trust_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A user-defined name of the trust config. TrustConfig names must be unique globally and match pattern `projects/*/locations/*/trustConfigs/*`. |
| `description` | `string` | One or more paragraphs of text description of a TrustConfig. |
| `updateTime` | `string` | Output only. The last update timestamp of a TrustConfig. |
| `createTime` | `string` | Output only. The creation timestamp of a TrustConfig. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `labels` | `object` | Set of labels associated with a TrustConfig. |
| `trustStores` | `array` | Set of trust stores to perform validation against. This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation. Only one TrustStore specified is currently allowed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, trustConfigsId` | Gets details of a single TrustConfig. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists TrustConfigs in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new TrustConfig in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, trustConfigsId` | Deletes a single TrustConfig. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists TrustConfigs in a given project and location. |
| `patch` | `EXEC` | `locationsId, projectsId, trustConfigsId` | Updates a TrustConfig. |
