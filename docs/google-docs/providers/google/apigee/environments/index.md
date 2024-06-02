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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the environment. Values must match the regular expression `^[.\\p&#123;Alnum&#125;-_]&#123;1,255&#125;$` |
| <CopyableCode code="description" /> | `string` | Optional. Description of the environment. |
| <CopyableCode code="apiProxyType" /> | `string` | Optional. API Proxy type supported by the environment. The type can be set when creating the Environment and cannot be changed. |
| <CopyableCode code="createdAt" /> | `string` | Output only. Creation time of this environment as milliseconds since epoch. |
| <CopyableCode code="deploymentType" /> | `string` | Optional. Deployment type supported by the environment. The deployment type can be set when creating the environment and cannot be changed. When you enable archive deployment, you will be **prevented from performing** a [subset of actions](/apigee/docs/api-platform/local-development/overview#prevented-actions) within the environment, including: * Managing the deployment of API proxy or shared flow revisions * Creating, updating, or deleting resource files * Creating, updating, or deleting target servers |
| <CopyableCode code="displayName" /> | `string` | Optional. Display name for this environment. |
| <CopyableCode code="forwardProxyUri" /> | `string` | Optional. URI of the forward proxy to be applied to the runtime instances in this environment. Must be in the format of &#123;scheme&#125;://&#123;hostname&#125;:&#123;port&#125;. Note that the scheme must be one of "http" or "https", and the port must be supplied. To remove a forward proxy setting, update the field to an empty value. Note: At this time, PUT operations to add forwardProxyUri to an existing environment fail if the environment has nodeConfig set up. To successfully add the forwardProxyUri setting in this case, include the NodeConfig details with the request. |
| <CopyableCode code="hasAttachedFlowHooks" /> | `boolean` |  |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. Last modification time of this environment as milliseconds since epoch. |
| <CopyableCode code="nodeConfig" /> | `object` | NodeConfig for setting the min/max number of nodes associated with the environment. |
| <CopyableCode code="properties" /> | `object` | Message for compatibility with legacy Edge specification for Java Properties object in JSON. |
| <CopyableCode code="state" /> | `string` | Output only. State of the environment. Values other than ACTIVE means the resource is not ready to use. |
| <CopyableCode code="type" /> | `string` | Optional. EnvironmentType selected for the environment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_get" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Gets environment details. |
| <CopyableCode code="organizations_environments_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates an environment in an organization. |
| <CopyableCode code="organizations_security_profiles_environments_create" /> | `INSERT` | <CopyableCode code="organizationsId, securityProfilesId" /> | CreateSecurityProfileEnvironmentAssociation creates profile environment association i.e. attaches environment to security profile. |
| <CopyableCode code="organizations_environments_delete" /> | `DELETE` | <CopyableCode code="environmentsId, organizationsId" /> | Deletes an environment from an organization. **Warning: You must delete all key value maps and key value entries before you delete an environment.** Otherwise, if you re-create the environment the key value map entry operations will encounter encryption/decryption discrepancies. |
| <CopyableCode code="organizations_security_profiles_environments_delete" /> | `DELETE` | <CopyableCode code="environmentsId, organizationsId, securityProfilesId" /> | DeleteSecurityProfileEnvironmentAssociation removes profile environment association i.e. detaches environment from security profile. |
| <CopyableCode code="organizations_environments_modify_environment" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId" /> | Updates properties for an Apigee environment with patch semantics using a field mask. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_environments_subscribe" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a subscription for the environment's Pub/Sub topic. The server will assign a random name for this subscription. The "name" and "push_config" must *not* be specified. |
| <CopyableCode code="organizations_environments_unsubscribe" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId" /> | Deletes a subscription for the environment's Pub/Sub topic. |
| <CopyableCode code="organizations_environments_update" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId" /> | Updates an existing environment. When updating properties, you must pass all existing properties to the API, even if they are not being changed. If you omit properties from the payload, the properties are removed. To get the current list of properties for the environment, use the [Get Environment API](get). **Note**: Both `PUT` and `POST` methods are supported for updating an existing environment. |
| <CopyableCode code="organizations_security_profiles_environments_compute_environment_scores" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, securityProfilesId" /> | ComputeEnvironmentScores calculates scores for requested time range for the specified security profile and environment. |
