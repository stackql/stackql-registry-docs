---
title: managed_zone_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_zone_operations
  - dns
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

Creates, updates, deletes, gets or lists a <code>managed_zone_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_zone_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.managed_zone_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the resource. This is the client_operation_id if the client specified it when the mutation was initiated, otherwise, it is generated by the server. The name must be 1-63 characters long and match the regular expression [-a-z0-9]? (output only) |
| <CopyableCode code="dnsKeyContext" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="startTime" /> | `string` | The time that this operation was started by the server. This is in RFC3339 text format (output only). |
| <CopyableCode code="status" /> | `string` | Status of the operation. Can be one of the following: "PENDING" or "DONE" (output only). A status of "DONE" means that the request to update the authoritative servers has been sent, but the servers might not be updated yet. |
| <CopyableCode code="type" /> | `string` | Type of the operation. Operations include insert, update, and delete (output only). |
| <CopyableCode code="user" /> | `string` | User who requested the operation, for example: user@example.com. cloud-dns-system for operations automatically done by the system. (output only) |
| <CopyableCode code="zoneContext" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedZone, operation, project" /> | Fetches the representation of an existing Operation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managedZone, project" /> | Enumerates Operations for the given ManagedZone. |

## `SELECT` examples

Enumerates Operations for the given ManagedZone.

```sql
SELECT
id,
dnsKeyContext,
kind,
startTime,
status,
type,
user,
zoneContext
FROM google.dns.managed_zone_operations
WHERE managedZone = '{{ managedZone }}'
AND project = '{{ project }}';
```
