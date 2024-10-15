---
title: custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_domains
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>custom_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.custom_domains" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_domains', value: 'view', },
        { label: 'custom_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appName" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="cert_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Custom domain of app resource payload. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Get the custom domain of one lifecycle application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | List the custom domains of one lifecycle application. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Create or update custom domain of one lifecycle application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Delete the custom domain of one lifecycle application. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="appName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Update custom domain of one lifecycle application. |

## `SELECT` examples

List the custom domains of one lifecycle application.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_domains', value: 'view', },
        { label: 'custom_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
appName,
app_name,
cert_name,
domainName,
provisioning_state,
resourceGroupName,
serviceName,
subscriptionId,
thumbprint
FROM azure.spring_apps.vw_custom_domains
WHERE appName = '{{ appName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.custom_domains
WHERE appName = '{{ appName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_domains</code> resource.

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
INSERT INTO azure.spring_apps.custom_domains (
appName,
domainName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ appName }}',
'{{ domainName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
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
        - name: thumbprint
          value: string
        - name: appName
          value: string
        - name: certName
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>custom_domains</code> resource.

```sql
/*+ update */
UPDATE azure.spring_apps.custom_domains
SET 
properties = '{{ properties }}'
WHERE 
appName = '{{ appName }}'
AND domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>custom_domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.custom_domains
WHERE appName = '{{ appName }}'
AND domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
