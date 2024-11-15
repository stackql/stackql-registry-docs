---
title: cas
hide_title: false
hide_table_of_contents: false
keywords:
  - cas
  - databases
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>cas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.cas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="certificate" /> | `string` | base64 encoding of the certificate used to secure database connections |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_get_ca" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To retrieve the public certificate used to secure the connection to the database cluster send a GET request to `/v2/databases/$DATABASE_ID/ca`. The response will be a JSON object with a `ca` key. This will be set to an object containing the base64 encoding of the public key certificate. |

## `SELECT` examples

To retrieve the public certificate used to secure the connection to the database cluster send a GET request to `/v2/databases/$DATABASE_ID/ca`. The response will be a JSON object with a `ca` key. This will be set to an object containing the base64 encoding of the public key certificate.


```sql
SELECT
certificate
FROM digitalocean.databases.cas
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```