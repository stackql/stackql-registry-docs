---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - apigee
  - google    
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the environment. Values must match the regular expression `^[.\\p{Alnum}-_]{1,255}$` |
| `description` | `string` | Optional. Description of the environment. |
| `state` | `string` | Output only. State of the environment. Values other than ACTIVE means the resource is not ready to use. |
| `displayName` | `string` | Optional. Display name for this environment. |
| `deploymentType` | `string` | Optional. Deployment type supported by the environment. The deployment type can be set when creating the environment and cannot be changed. When you enable archive deployment, you will be **prevented from performing** a [subset of actions](/apigee/docs/api-platform/local-development/overview#prevented-actions) within the environment, including: * Managing the deployment of API proxy or shared flow revisions * Creating, updating, or deleting resource files * Creating, updating, or deleting target servers |
| `forwardProxyUri` | `string` | Optional. Url of the forward proxy to be applied to the runtime instances in this environment. Must be in the format of {scheme}://{hostname}:{port}. Note that scheme must be one of "http" or "https", and port must be supplied. |
| `properties` | `object` | Message for compatibility with legacy Edge specification for Java Properties object in JSON. |
| `createdAt` | `string` | Output only. Creation time of this environment as milliseconds since epoch. |
| `apiProxyType` | `string` | Optional. API Proxy type supported by the environment. The type can be set when creating the Environment and cannot be changed. |
| `lastModifiedAt` | `string` | Output only. Last modification time of this environment as milliseconds since epoch. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_get` | `SELECT` | `environmentsId, organizationsId` | Gets environment details. |
| `organizations_environments_create` | `INSERT` | `organizationsId` | Creates an environment in an organization. |
| `organizations_securityProfiles_environments_create` | `INSERT` | `organizationsId, securityProfilesId` | CreateSecurityProfileEnvironmentAssociation creates profile environment association i.e. attaches environment to security profile. |
| `organizations_environments_delete` | `DELETE` | `environmentsId, organizationsId` | Deletes an environment from an organization. **Note**: You must delete all key value maps and key value entries before you can delete an environment. |
| `organizations_securityProfiles_environments_delete` | `DELETE` | `environmentsId, organizationsId, securityProfilesId` | DeleteSecurityProfileEnvironmentAssociation removes profile environment association i.e. detaches environment from security profile. |
| `organizations_environments_subscribe` | `EXEC` | `environmentsId, organizationsId` | Creates a subscription for the environment's Pub/Sub topic. The server will assign a random name for this subscription. The "name" and "push_config" must *not* be specified. |
| `organizations_environments_unsubscribe` | `EXEC` | `environmentsId, organizationsId` | Deletes a subscription for the environment's Pub/Sub topic. |
| `organizations_environments_update` | `EXEC` | `environmentsId, organizationsId` | Updates an existing environment. When updating properties, you must pass all existing properties to the API, even if they are not being changed. If you omit properties from the payload, the properties are removed. To get the current list of properties for the environment, use the [Get Environment API](get). **Note**: Both `PUT` and `POST` methods are supported for updating an existing environment. |
| `organizations_environments_updateDebugmask` | `EXEC` | `environmentsId, organizationsId` | Updates the debug mask singleton resource for an environment. |
| `organizations_environments_updateEnvironment` | `EXEC` | `environmentsId, organizationsId` | Updates an existing environment. When updating properties, you must pass all existing properties to the API, even if they are not being changed. If you omit properties from the payload, the properties are removed. To get the current list of properties for the environment, use the [Get Environment API](get). **Note**: Both `PUT` and `POST` methods are supported for updating an existing environment. |
| `organizations_environments_updateTraceConfig` | `EXEC` | `environmentsId, organizationsId` | Updates the trace configurations in an environment. Note that the repeated fields have replace semantics when included in the field mask and that they will be overwritten by the value of the fields in the request body. |
| `organizations_securityProfiles_environments_computeEnvironmentScores` | `EXEC` | `environmentsId, organizationsId, securityProfilesId` | ComputeEnvironmentScores calculates scores for requested time range for the specified security profile and environment. |
