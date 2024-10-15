---
title: static_site_users
hide_title: false
hide_table_of_contents: false
keywords:
  - static_site_users
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

Creates, updates, deletes, gets or lists a <code>static_site_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_site_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.static_site_users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | StaticSiteUserARMResource resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authprovider, name, resourceGroupName, subscriptionId" /> | Description for Gets the list of users of a static site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authprovider, name, resourceGroupName, subscriptionId, userid" /> | Description for Deletes the user entry from the static site. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="authprovider, name, resourceGroupName, subscriptionId, userid" /> | Description for Updates a user entry with the listed roles |

## `SELECT` examples

Description for Gets the list of users of a static site.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.static_site_users
WHERE authprovider = '{{ authprovider }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `UPDATE` example

Updates a <code>static_site_users</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.static_site_users
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
authprovider = '{{ authprovider }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userid = '{{ userid }}';
```

## `DELETE` example

Deletes the specified <code>static_site_users</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.static_site_users
WHERE authprovider = '{{ authprovider }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userid = '{{ userid }}';
```
