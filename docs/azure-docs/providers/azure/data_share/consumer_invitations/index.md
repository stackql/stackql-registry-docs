---
title: consumer_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_invitations
  - data_share
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

Creates, updates, deletes, gets or lists a <code>consumer_invitations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.consumer_invitations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_consumer_invitations', value: 'view', },
        { label: 'consumer_invitations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `text` | Name of the azure resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_set_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="invitationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="invitation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="invitation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_tenant_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="responded_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="sent_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="terms_of_use" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the azure resource |
| <CopyableCode code="user_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="properties" /> | `object` | Properties of consumer invitation |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="invitationId, location" /> | Get an invitation |
| <CopyableCode code="list_invitations" /> | `SELECT` | <CopyableCode code="" /> | Lists invitations |
| <CopyableCode code="reject_invitation" /> | `EXEC` | <CopyableCode code="location, data__properties" /> | Reject an invitation |

## `SELECT` examples

Lists invitations

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_consumer_invitations', value: 'view', },
        { label: 'consumer_invitations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
data_set_count,
expiration_date,
invitationId,
invitation_id,
invitation_status,
location,
provider_email,
provider_name,
provider_tenant_name,
responded_at,
sent_at,
share_name,
system_data,
terms_of_use,
type,
user_email,
user_name
FROM azure.data_share.vw_consumer_invitations
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_share.consumer_invitations
;
```
</TabItem></Tabs>

