---
title: apps_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - apps_runtimes
  - appengine
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

Creates, updates, deletes, gets or lists a <code>apps_runtimes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.appengine.apps_runtimes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the runtime, e.g., 'go113', 'nodejs12', etc. |
| <CopyableCode code="decommissionedDate" /> | `object` | Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: A full date, with non-zero year, month, and day values. A month and day, with a zero year (for example, an anniversary). A year on its own, with a zero month and a zero day. A year and month, with a zero day (for example, a credit card expiration date).Related types: google.type.TimeOfDay google.type.DateTime google.protobuf.Timestamp |
| <CopyableCode code="deprecationDate" /> | `object` | Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: A full date, with non-zero year, month, and day values. A month and day, with a zero year (for example, an anniversary). A year on its own, with a zero month and a zero day. A year and month, with a zero day (for example, a credit card expiration date).Related types: google.type.TimeOfDay google.type.DateTime google.protobuf.Timestamp |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name, e.g. 'Node.js 12', etc. |
| <CopyableCode code="endOfSupportDate" /> | `object` | Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: A full date, with non-zero year, month, and day values. A month and day, with a zero year (for example, an anniversary). A year on its own, with a zero month and a zero day. A year and month, with a zero day (for example, a credit card expiration date).Related types: google.type.TimeOfDay google.type.DateTime google.protobuf.Timestamp |
| <CopyableCode code="environment" /> | `string` | The environment of the runtime. |
| <CopyableCode code="stage" /> | `string` | The stage of life this runtime is in, e.g., BETA, GA, etc. |
| <CopyableCode code="supportedOperatingSystems" /> | `array` | Supported operating systems for the runtime, e.g., 'ubuntu22', etc. |
| <CopyableCode code="warnings" /> | `array` | Warning messages, e.g., a deprecation warning. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_runtimes" /> | `SELECT` | <CopyableCode code="appsId" /> | Lists all the available runtimes for the application. |

## `SELECT` examples

Lists all the available runtimes for the application.

```sql
SELECT
name,
decommissionedDate,
deprecationDate,
displayName,
endOfSupportDate,
environment,
stage,
supportedOperatingSystems,
warnings
FROM google.appengine.apps_runtimes
WHERE appsId = '{{ appsId }}';
```
