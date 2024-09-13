
---
title: instances_serial_port_output
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_serial_port_output
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

Creates, updates, deletes or gets an <code>instances_serial_port_output</code> resource or lists <code>instances_serial_port_output</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_serial_port_output</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_serial_port_output" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contents" /> | `string` | [Output Only] The contents of the console output. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#serialPortOutput for serial port output. |
| <CopyableCode code="next" /> | `string` | [Output Only] The position of the next byte of content, regardless of whether the content exists, following the output returned in the `contents` property. Use this value in the next request as the start parameter. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for this resource. |
| <CopyableCode code="start" /> | `string` | The starting byte position of the output that was returned. This should match the start parameter sent with the request. If the serial console output exceeds the size of the buffer (1 MB), older output is overwritten by newer content. The output start value will indicate the byte position of the output that was returned, which might be different than the `start` value that was specified in the request. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_serial_port_output" /> | `SELECT` | <CopyableCode code="instance, project, zone" /> | Returns the last 1 MB of serial port output from the specified instance. |

## `SELECT` examples

Returns the last 1 MB of serial port output from the specified instance.

```sql
SELECT
contents,
kind,
next,
selfLink,
start
FROM google.compute.instances_serial_port_output
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}'; 
```
