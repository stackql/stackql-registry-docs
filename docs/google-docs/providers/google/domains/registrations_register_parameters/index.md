---
title: registrations_register_parameters
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations_register_parameters
  - domains
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

Creates, updates, deletes, gets or lists a <code>registrations_register_parameters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registrations_register_parameters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.domains.registrations_register_parameters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="registerParameters" /> | `object` | Parameters required to register a new domain. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="retrieve_register_parameters" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`. |

## `SELECT` examples

Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`.

```sql
SELECT
registerParameters
FROM google.domains.registrations_register_parameters
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
