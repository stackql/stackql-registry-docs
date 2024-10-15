---
title: kube_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - kube_environments
  - app_service
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

Creates, updates, deletes, gets or lists a <code>kube_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kube_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.kube_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="extendedLocation" /> | `object` | Extended Location. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | KubeEnvironment resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get the properties of a Kubernetes Environment. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Get all the Kubernetes Environments in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all Kubernetes Environments for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates or updates a Kubernetes Environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Delete a Kubernetes Environment. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates or updates a Kubernetes Environment. |

## `SELECT` examples

Description for Get all Kubernetes Environments for a subscription.


```sql
SELECT
id,
name,
extendedLocation,
kind,
location,
properties,
tags,
type
FROM azure.app_service.kube_environments
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kube_environments</code> resource.

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
INSERT INTO azure.app_service.kube_environments (
name,
resourceGroupName,
subscriptionId,
kind,
location,
tags,
properties,
extendedLocation
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: deploymentErrors
          value: string
        - name: internalLoadBalancerEnabled
          value: boolean
        - name: defaultDomain
          value: string
        - name: staticIp
          value: string
        - name: environmentType
          value: string
        - name: arcConfiguration
          value:
            - name: artifactsStorageType
              value: string
            - name: artifactStorageClassName
              value: string
            - name: artifactStorageMountPath
              value: string
            - name: artifactStorageNodeName
              value: string
            - name: artifactStorageAccessMode
              value: string
            - name: frontEndServiceConfiguration
              value:
                - name: kind
                  value: string
            - name: kubeConfig
              value: string
        - name: appLogsConfiguration
          value:
            - name: destination
              value: string
            - name: logAnalyticsConfiguration
              value:
                - name: customerId
                  value: string
                - name: sharedKey
                  value: string
        - name: containerAppsConfiguration
          value:
            - name: daprAIInstrumentationKey
              value: string
            - name: platformReservedCidr
              value: string
            - name: platformReservedDnsIP
              value: string
            - name: controlPlaneSubnetResourceId
              value: string
            - name: appSubnetResourceId
              value: string
            - name: dockerBridgeCidr
              value: string
        - name: aksResourceID
          value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>kube_environments</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.kube_environments
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>kube_environments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.kube_environments
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
