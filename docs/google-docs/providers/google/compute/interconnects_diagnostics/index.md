---
title: interconnects_diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - interconnects_diagnostics
  - compute
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

Creates, updates, deletes, gets or lists a <code>interconnects_diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interconnects_diagnostics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.interconnects_diagnostics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="result" /> | `object` | Diagnostics information about the Interconnect connection, which contains detailed and current technical information about Google's side of the connection. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_diagnostics" /> | `SELECT` | <CopyableCode code="interconnect, project" /> | Returns the interconnectDiagnostics for the specified Interconnect. In the event of a global outage, do not use this API to make decisions about where to redirect your network traffic. Unlike a VLAN attachment, which is regional, a Cloud Interconnect connection is a global resource. A global outage can prevent this API from functioning properly. |

## `SELECT` examples

Returns the interconnectDiagnostics for the specified Interconnect. In the event of a global outage, do not use this API to make decisions about where to redirect your network traffic. Unlike a VLAN attachment, which is regional, a Cloud Interconnect connection is a global resource. A global outage can prevent this API from functioning properly.

```sql
SELECT
result
FROM google.compute.interconnects_diagnostics
WHERE interconnect = '{{ interconnect }}'
AND project = '{{ project }}'; 
```
