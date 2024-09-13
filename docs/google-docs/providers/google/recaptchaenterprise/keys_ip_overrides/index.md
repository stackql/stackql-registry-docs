---
title: keys_ip_overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_ip_overrides
  - recaptchaenterprise
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

Creates, updates, deletes or gets an <code>keys_ip_override</code> resource or lists <code>keys_ip_overrides</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_ip_overrides</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.keys_ip_overrides" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ip" /> | `string` | Required. The IP address to override (can be IPv4, IPv6 or CIDR). The IP override must be a valid IPv4 or IPv6 address, or a CIDR range. The IP override must be a public IP address. Example of IPv4: 168.192.5.6 Example of IPv6: 2001:0000:130F:0000:0000:09C0:876A:130B Example of IPv4 with CIDR: 168.192.5.0/24 Example of IPv6 with CIDR: 2001:0DB8:1234::/48 |
| <CopyableCode code="overrideType" /> | `string` | Required. Describes the type of IP override. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_ip_overrides" /> | `SELECT` | <CopyableCode code="keysId, projectsId" /> | Lists all IP overrides for a key. |

## `SELECT` examples

Lists all IP overrides for a key.

```sql
SELECT
ip,
overrideType
FROM google.recaptchaenterprise.keys_ip_overrides
WHERE keysId = '{{ keysId }}'
AND projectsId = '{{ projectsId }}'; 
```
