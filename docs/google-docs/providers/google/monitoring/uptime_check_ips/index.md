---
title: uptime_check_ips
hide_title: false
hide_table_of_contents: false
keywords:
  - uptime_check_ips
  - monitoring
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

Creates, updates, deletes or gets an <code>uptime_check_ip</code> resource or lists <code>uptime_check_ips</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>uptime_check_ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.uptime_check_ips" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ipAddress" /> | `string` | The IP address from which the Uptime check originates. This is a fully specified IP address (not an IP address range). Most IP addresses, as of this publication, are in IPv4 format; however, one should not rely on the IP addresses being in IPv4 format indefinitely, and should support interpreting this field in either IPv4 or IPv6 format. |
| <CopyableCode code="location" /> | `string` | A more specific location within the region that typically encodes a particular city/town/metro (and its containing state/province or country) within the broader umbrella region category. |
| <CopyableCode code="region" /> | `string` | A broad region category in which the IP address is located. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="uptime_check_ips_list" /> | `SELECT` | <CopyableCode code="" /> | Returns the list of IP addresses that checkers run from. |

## `SELECT` examples

Returns the list of IP addresses that checkers run from.

```sql
SELECT
ipAddress,
location,
region
FROM google.monitoring.uptime_check_ips
WHERE  = '{{  }}'; 
```
