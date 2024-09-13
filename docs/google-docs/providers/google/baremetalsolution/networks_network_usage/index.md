---
title: networks_network_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - networks_network_usage
  - baremetalsolution
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

Creates, updates, deletes or gets an <code>networks_network_usage</code> resource or lists <code>networks_network_usage</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks_network_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.baremetalsolution.networks_network_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="networks" /> | `array` | Networks with IPs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_network_usage" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all Networks (and used IPs for each Network) in the vendor account associated with the specified project. |

## `SELECT` examples

List all Networks (and used IPs for each Network) in the vendor account associated with the specified project.

```sql
SELECT
networks
FROM google.baremetalsolution.networks_network_usage
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
