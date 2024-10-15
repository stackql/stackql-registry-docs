---
title: api_portal_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - api_portal_custom_domains
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

Creates, updates, deletes, gets or lists a <code>api_portal_custom_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_portal_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.api_portal_custom_domains" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_portal_custom_domains', value: 'view', },
        { label: 'api_portal_custom_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiPortalName" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of custom domain for API portal |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiPortalName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Get the API portal custom domain. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apiPortalName, resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all API portal custom domains. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiPortalName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Create or update the API portal custom domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiPortalName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Delete the API portal custom domain. |

## `SELECT` examples

Handle requests to list all API portal custom domains.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_portal_custom_domains', value: 'view', },
        { label: 'api_portal_custom_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiPortalName,
domainName,
resourceGroupName,
serviceName,
subscriptionId,
thumbprint
FROM azure.spring_apps.vw_api_portal_custom_domains
WHERE apiPortalName = '{{ apiPortalName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.api_portal_custom_domains
WHERE apiPortalName = '{{ apiPortalName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_portal_custom_domains</code> resource.

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
INSERT INTO azure.spring_apps.api_portal_custom_domains (
apiPortalName,
domainName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiPortalName }}',
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>api_portal_custom_domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.api_portal_custom_domains
WHERE apiPortalName = '{{ apiPortalName }}'
AND domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
