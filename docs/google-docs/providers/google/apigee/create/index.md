---
title: create
hide_title: false
hide_table_of_contents: false
keywords:
  - create
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

Creates, updates, deletes, gets or lists a <code>create</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>create</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.create" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_developers_apps_keys_create_create" /> | `INSERT` | <CopyableCode code="appsId, developersId, organizationsId" /> | Creates a custom consumer key and secret for a developer app. This is particularly useful if you want to migrate existing consumer keys and secrets to Apigee from another system. Consumer keys and secrets can contain letters, numbers, underscores, and hyphens. No other special characters are allowed. To avoid service disruptions, a consumer key and secret should not exceed 2 KBs each. **Note**: When creating the consumer key and secret, an association to API products will not be made. Therefore, you should not specify the associated API products in your request. Instead, use the UpdateDeveloperAppKey API to make the association after the consumer key and secret are created. If a consumer key and secret already exist, you can keep them or delete them using the DeleteDeveloperAppKey API. **Note**: All keys start out with status=approved, even if status=revoked is passed when the key is created. To revoke a key, use the UpdateDeveloperAppKey API. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>create</code> resource.

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
INSERT INTO google.apigee.create (
appsId,
developersId,
organizationsId,
consumerKey,
apiProducts,
consumerSecret,
issuedAt,
scopes,
status,
expiresAt,
attributes,
expiresInSeconds
)
SELECT 
'{{ appsId }}',
'{{ developersId }}',
'{{ organizationsId }}',
'{{ consumerKey }}',
'{{ apiProducts }}',
'{{ consumerSecret }}',
'{{ issuedAt }}',
'{{ scopes }}',
'{{ status }}',
'{{ expiresAt }}',
'{{ attributes }}',
'{{ expiresInSeconds }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
consumerKey: string
apiProducts:
  - type: string
consumerSecret: string
issuedAt: string
scopes:
  - type: string
status: string
expiresAt: string
attributes:
  - name: string
    value: string
expiresInSeconds: string

```
</TabItem>
</Tabs>
