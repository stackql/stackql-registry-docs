
---
title: connections_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - connections_connection
  - servicenetworking
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

Creates, updates, deletes or gets an <code>connections_connection</code> resource or lists <code>connections_connection</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.connections_connection" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_connection" /> | `DELETE` | <CopyableCode code="connectionsId, servicesId" /> | Deletes a private service access connection. |

## `DELETE` example

Deletes the specified connections_connection resource.

```sql
DELETE FROM google.servicenetworking.connections_connection
WHERE connectionsId = '{{ connectionsId }}'
AND servicesId = '{{ servicesId }}';
```
