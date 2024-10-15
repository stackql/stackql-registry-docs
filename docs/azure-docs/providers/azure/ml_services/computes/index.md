---
title: computes
hide_title: false
hide_table_of_contents: false
keywords:
  - computes
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>computes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>computes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.computes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_computes', value: 'view', },
        { label: 'computes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="computeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="is_attached_compute" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Specifies the location of the resource. |
| <CopyableCode code="modified_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | Specifies the location of the resource. |
| <CopyableCode code="properties" /> | `object` | Machine Learning compute object. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, workspaceName" /> | Gets compute definition by its name. Any secrets (storage keys, service credentials, etc) are not returned - use 'keys' nested resource to get them. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets computes in specified workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, underlyingResourceAction, workspaceName" /> | Deletes specified Machine Learning compute. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, workspaceName" /> | Updates properties of a compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. |
| <CopyableCode code="resize" /> | `EXEC` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, workspaceName" /> | Updates the size of a Compute Instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, workspaceName" /> | Posts a restart action to a compute instance |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, workspaceName" /> | Posts a start action to a compute instance |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, workspaceName" /> | Posts a stop action to a compute instance |

## `SELECT` examples

Gets computes in specified workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_computes', value: 'view', },
        { label: 'computes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
computeName,
compute_location,
compute_type,
created_on,
disable_local_auth,
identity,
is_attached_compute,
location,
modified_on,
provisioning_errors,
provisioning_state,
resourceGroupName,
resource_id,
sku,
subscriptionId,
system_data,
tags,
type,
workspaceName
FROM azure.ml_services.vw_computes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.ml_services.computes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>computes</code> resource.

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
INSERT INTO azure.ml_services.computes (
computeName,
resourceGroupName,
subscriptionId,
workspaceName,
properties,
identity,
location,
tags,
sku
)
SELECT 
'{{ computeName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}',
'{{ identity }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}'
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
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: computeType
          value: []
        - name: computeLocation
          value: string
        - name: provisioningState
          value: string
        - name: description
          value: string
        - name: createdOn
          value: string
        - name: modifiedOn
          value: string
        - name: resourceId
          value: string
        - name: provisioningErrors
          value:
            - - name: error
                value:
                  - name: code
                    value: string
                  - name: message
                    value: string
                  - name: target
                    value: string
                  - name: details
                    value:
                      - - name: code
                          value: string
                        - name: message
                          value: string
                        - name: target
                          value: string
                        - name: details
                          value:
                            - - name: code
                                value: string
                              - name: message
                                value: string
                              - name: target
                                value: string
                              - name: details
                                value:
                                  - - name: code
                                      value: string
                                    - name: message
                                      value: string
                                    - name: target
                                      value: string
                                    - name: details
                                      value:
                                        - - name: code
                                            value: string
                                          - name: message
                                            value: string
                                          - name: target
                                            value: string
                                          - name: details
                                            value:
                                              - - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                                - name: target
                                                  value: string
                                                - name: details
                                                  value:
                                                    - - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                      - name: target
                                                        value: string
                                                      - name: details
                                                        value:
                                                          - - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                            - name: target
                                                              value: string
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: additionalInfo
                                                              value:
                                                                - []
                                                      - name: additionalInfo
                                                        value:
                                                          - - name: type
                                                              value: string
                                                            - name: info
                                                              value: object
                                                - name: additionalInfo
                                                  value:
                                                    - - name: type
                                                        value: string
                                                      - name: info
                                                        value: object
                                          - name: additionalInfo
                                            value:
                                              - - name: type
                                                  value: string
                                                - name: info
                                                  value: object
                                    - name: additionalInfo
                                      value:
                                        - - name: type
                                            value: string
                                          - name: info
                                            value: object
                              - name: additionalInfo
                                value:
                                  - - name: type
                                      value: string
                                    - name: info
                                      value: object
                        - name: additionalInfo
                          value:
                            - - name: type
                                value: string
                              - name: info
                                value: object
                  - name: additionalInfo
                    value:
                      - - name: type
                          value: string
                        - name: info
                          value: object
        - name: isAttachedCompute
          value: boolean
        - name: disableLocalAuth
          value: boolean
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: location
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>computes</code> resource.

```sql
/*+ update */
UPDATE azure.ml_services.computes
SET 
properties = '{{ properties }}'
WHERE 
computeName = '{{ computeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>computes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.computes
WHERE computeName = '{{ computeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND underlyingResourceAction = '{{ underlyingResourceAction }}'
AND workspaceName = '{{ workspaceName }}';
```
