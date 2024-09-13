---
title: interconnects_macsec_config
hide_title: false
hide_table_of_contents: false
keywords:
  - interconnects_macsec_config
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

Creates, updates, deletes, gets or lists a <code>interconnects_macsec_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interconnects_macsec_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.interconnects_macsec_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | end_interface: MixerGetResponseWithEtagBuilder |
| <CopyableCode code="result" /> | `object` | MACsec configuration information for the Interconnect connection. Contains the generated Connectivity Association Key Name (CKN) and the key (CAK) for this Interconnect connection. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_macsec_config" /> | `SELECT` | <CopyableCode code="interconnect, project" /> | Returns the interconnectMacsecConfig for the specified Interconnect. |

## `SELECT` examples

Returns the interconnectMacsecConfig for the specified Interconnect.

```sql
SELECT
etag,
result
FROM google.compute.interconnects_macsec_config
WHERE interconnect = '{{ interconnect }}'
AND project = '{{ project }}'; 
```
