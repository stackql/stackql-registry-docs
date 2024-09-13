---
title: keys_app_group_app_key
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_app_group_app_key
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>keys_app_group_app_key</code> resource or lists <code>keys_app_group_app_key</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_app_group_app_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.keys_app_group_app_key" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_appgroups_apps_keys_update_app_group_app_key" /> | `UPDATE` | <CopyableCode code="appgroupsId, appsId, keysId, organizationsId" /> | Adds an API product to an AppGroupAppKey, enabling the app that holds the key to access the API resources bundled in the API product. In addition, you can add attributes to the AppGroupAppKey. This API replaces the existing attributes with those specified in the request. Include or exclude any existing attributes that you want to retain or delete, respectively. You can use the same key to access all API products associated with the app. |

## `UPDATE` example

Updates a keys_app_group_app_key only if the necessary resources are available.

```sql
UPDATE google.apigee.keys_app_group_app_key
SET 
apiProducts = '{{ apiProducts }}',
appGroupAppKey = '{{ appGroupAppKey }}',
action = '{{ action }}'
WHERE 
appgroupsId = '{{ appgroupsId }}'
AND appsId = '{{ appsId }}'
AND keysId = '{{ keysId }}'
AND organizationsId = '{{ organizationsId }}';
```
