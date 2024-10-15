---
title: email_services_verified_exchange_online_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - email_services_verified_exchange_online_domains
  - communication
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

Creates, updates, deletes, gets or lists a <code>email_services_verified_exchange_online_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_services_verified_exchange_online_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.email_services_verified_exchange_online_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of domains that are fully verified in Exchange Online. |

## `SELECT` examples

Get a list of domains that are fully verified in Exchange Online.


```sql
SELECT
column_anon
FROM azure.communication.email_services_verified_exchange_online_domains
WHERE subscriptionId = '{{ subscriptionId }}';
```