---
title: provider_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_shares
  - stream_sharing
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.stream_sharing.provider_shares" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="_cloud_cluster" /> | `` |  |
| <CopyableCode code="_service_account" /> | `` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="cloud_cluster" /> | `object` | The cloud cluster to which this belongs. |
| <CopyableCode code="consumer_organization_name" /> | `string` | Consumer organization name |
| <CopyableCode code="consumer_restriction" /> | `` | Restrictions on the consumer that can redeem this token |
| <CopyableCode code="consumer_user_name" /> | `string` | Name of the consumer |
| <CopyableCode code="delivery_method" /> | `string` | Method by which the invite will be delivered |
| <CopyableCode code="invite_expires_at" /> | `string` | The date and time at which the invitation will expire. Only for invited shares |
| <CopyableCode code="invited_at" /> | `string` | The date and time at which consumer was invited |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="provider_user" /> | `object` | The provider user/inviter |
| <CopyableCode code="provider_user_name" /> | `string` | Name or email of the provider user. Deprecated |
| <CopyableCode code="redeemed_at" /> | `string` | The date and time at which the invite was redeemed |
| <CopyableCode code="service_account" /> | `object` | The service account associated with this object. |
| <CopyableCode code="status" /> | `object` | The status of the Provider Share |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cdx_v1provider_share" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read a provider share. |
| <CopyableCode code="list_cdx_v1provider_shares" /> | `SELECT` |  | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all provider shares. |
| <CopyableCode code="create_cdx_v1provider_share" /> | `INSERT` |  | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Creates a share based on delivery method. |
| <CopyableCode code="delete_cdx_v1provider_share" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to delete a provider share. |
| <CopyableCode code="resend_cdx_v1provider_share" /> | `EXEC` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Resend provider share |
