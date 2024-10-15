---
title: static_site_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - static_site_custom_domains
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

Creates, updates, deletes, gets or lists a <code>static_site_custom_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_site_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.static_site_custom_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | StaticSiteCustomDomainOverviewARMResource resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Gets an existing custom domain for a particular static site. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets all static site custom domains for a particular static site. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Creates a new static site custom domain in an existing resource group and static site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Deletes a custom domain. |

## `SELECT` examples

Description for Gets all static site custom domains for a particular static site.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.static_site_custom_domains
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>static_site_custom_domains</code> resource.

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
INSERT INTO azure.app_service.static_site_custom_domains (
domainName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ domainName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ properties }}'
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
    - name: type
      value: string
    - name: properties
      value:
        - name: validationMethod
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>static_site_custom_domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.static_site_custom_domains
WHERE domainName = '{{ domainName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
