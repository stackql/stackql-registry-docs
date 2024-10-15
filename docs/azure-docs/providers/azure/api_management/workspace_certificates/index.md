---
title: workspace_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_certificates
  - api_management
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

Creates, updates, deletes, gets or lists a <code>workspace_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_certificates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_certificates', value: 'view', },
        { label: 'workspace_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="certificateId" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subject" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the Certificate contract. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the certificate specified by its identifier. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of all certificates in the specified workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or updates the certificate being used for authentication with the backend. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, certificateId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes specific certificate. |
| <CopyableCode code="refresh_secret" /> | `EXEC` | <CopyableCode code="certificateId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | From KeyVault, Refresh the certificate being used for authentication with the backend. |

## `SELECT` examples

Lists a collection of all certificates in the specified workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_certificates', value: 'view', },
        { label: 'workspace_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
certificateId,
expiration_date,
key_vault,
resourceGroupName,
serviceName,
subject,
subscriptionId,
thumbprint,
workspaceId
FROM azure.api_management.vw_workspace_certificates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.workspace_certificates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_certificates</code> resource.

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
INSERT INTO azure.api_management.workspace_certificates (
certificateId,
resourceGroupName,
serviceName,
subscriptionId,
workspaceId,
properties
)
SELECT 
'{{ certificateId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ workspaceId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: data
          value: string
        - name: password
          value: string
        - name: keyVault
          value:
            - name: secretIdentifier
              value: string
            - name: identityClientId
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>workspace_certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_certificates
WHERE If-Match = '{{ If-Match }}'
AND certificateId = '{{ certificateId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
