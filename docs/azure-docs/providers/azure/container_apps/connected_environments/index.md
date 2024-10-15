---
title: connected_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments
  - container_apps
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>connected_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connected_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.connected_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | ConnectedEnvironment resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Get the properties of an connectedEnvironment. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all connectedEnvironments in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all connectedEnvironments for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Creates or updates an connectedEnvironment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Delete an connectedEnvironment. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Patches a Managed Environment. Only patching of tags is supported currently |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Checks if resource connectedEnvironmentName is available. |

## `SELECT` examples

Get all connectedEnvironments for a subscription.


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.container_apps.connected_environments
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connected_environments</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.container_apps.connected_environments (
connectedEnvironmentName,
resourceGroupName,
subscriptionId,
tags,
location,
extendedLocation,
properties
)
SELECT 
'{{ connectedEnvironmentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: deploymentErrors
          value: string
        - name: defaultDomain
          value: string
        - name: staticIp
          value: string
        - name: daprAIConnectionString
          value: string
        - name: customDomainConfiguration
          value:
            - name: customDomainVerificationId
              value: string
            - name: dnsSuffix
              value: string
            - name: certificateKeyVaultProperties
              value:
                - name: identity
                  value: string
                - name: keyVaultUrl
                  value: string
            - name: certificateValue
              value: string
            - name: certificatePassword
              value: string
            - name: expirationDate
              value: string
            - name: thumbprint
              value: string
            - name: subjectName
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connected_environments</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.connected_environments
SET 

WHERE 
connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>connected_environments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.connected_environments
WHERE connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
