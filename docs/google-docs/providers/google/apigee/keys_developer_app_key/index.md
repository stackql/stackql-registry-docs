---
title: keys_developer_app_key
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_developer_app_key
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

Creates, updates, deletes, gets or lists a <code>keys_developer_app_key</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_developer_app_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.keys_developer_app_key" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_developers_apps_keys_update_developer_app_key" /> | `UPDATE` | <CopyableCode code="appsId, developersId, keysId, organizationsId" /> | Adds an API product to a developer app key, enabling the app that holds the key to access the API resources bundled in the API product. In addition, you can add attributes to a developer app key. This API replaces the existing attributes with those specified in the request. Include or exclude any existing attributes that you want to retain or delete, respectively. You can use the same key to access all API products associated with the app. |

## `UPDATE` example

Updates a <code>keys_developer_app_key</code> resource.

```sql
/*+ update */
UPDATE google.apigee.keys_developer_app_key
SET 
consumerKey = '{{ consumerKey }}',
apiProducts = '{{ apiProducts }}',
consumerSecret = '{{ consumerSecret }}',
issuedAt = '{{ issuedAt }}',
scopes = '{{ scopes }}',
status = '{{ status }}',
expiresAt = '{{ expiresAt }}',
attributes = '{{ attributes }}',
expiresInSeconds = '{{ expiresInSeconds }}'
WHERE 
appsId = '{{ appsId }}'
AND developersId = '{{ developersId }}'
AND keysId = '{{ keysId }}'
AND organizationsId = '{{ organizationsId }}';
```
