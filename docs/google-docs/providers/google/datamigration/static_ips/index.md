---
title: static_ips
hide_title: false
hide_table_of_contents: false
keywords:
  - static_ips
  - datamigration
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

Creates, updates, deletes, gets or lists a <code>static_ips</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datamigration.static_ips" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextPageToken" /> | `string` | A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| <CopyableCode code="staticIps" /> | `array` | List of static IPs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_static_ips" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method. |

## `SELECT` examples

Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method.

```sql
SELECT
nextPageToken,
staticIps
FROM google.datamigration.static_ips
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
