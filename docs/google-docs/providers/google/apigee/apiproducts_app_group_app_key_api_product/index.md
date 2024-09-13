
---
title: apiproducts_app_group_app_key_api_product
hide_title: false
hide_table_of_contents: false
keywords:
  - apiproducts_app_group_app_key_api_product
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

Creates, updates, deletes or gets an <code>apiproducts_app_group_app_key_api_product</code> resource or lists <code>apiproducts_app_group_app_key_api_product</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apiproducts_app_group_app_key_api_product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.apiproducts_app_group_app_key_api_product" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_appgroups_apps_keys_apiproducts_update_app_group_app_key_api_product" /> | `UPDATE` | <CopyableCode code="apiproductsId, appgroupsId, appsId, keysId, organizationsId" /> | Approves or revokes the consumer key for an API product. After a consumer key is approved, the app can use it to access APIs. A consumer key that is revoked or pending cannot be used to access an API. Any access tokens associated with a revoked consumer key will remain active. However, Apigee checks the status of the consumer key and if set to `revoked` will not allow access to the API. |

## `UPDATE` example

Updates a apiproducts_app_group_app_key_api_product only if the necessary resources are available.

```sql
UPDATE google.apigee.apiproducts_app_group_app_key_api_product
SET 

WHERE 
apiproductsId = '{{ apiproductsId }}'
AND appgroupsId = '{{ appgroupsId }}'
AND appsId = '{{ appsId }}'
AND keysId = '{{ keysId }}'
AND organizationsId = '{{ organizationsId }}';
```
