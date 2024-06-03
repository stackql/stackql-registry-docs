---
title: supported_database_flags
hide_title: false
hide_table_of_contents: false
keywords:
  - supported_database_flags
  - alloydb
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>supported_database_flags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.supported_database_flags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the flag resource, following Google Cloud conventions, e.g.: * projects/&#123;project&#125;/locations/&#123;location&#125;/flags/&#123;flag&#125; This field currently has no semantic meaning. |
| <CopyableCode code="acceptsMultipleValues" /> | `boolean` | Whether the database flag accepts multiple values. If true, a comma-separated list of stringified values may be specified. |
| <CopyableCode code="flagName" /> | `string` | The name of the database flag, e.g. "max_allowed_packets". The is a possibly key for the Instance.database_flags map field. |
| <CopyableCode code="integerRestrictions" /> | `object` | Restrictions on INTEGER type values. |
| <CopyableCode code="requiresDbRestart" /> | `boolean` | Whether setting or updating this flag on an Instance requires a database restart. If a flag that requires database restart is set, the backend will automatically restart the database (making sure to satisfy any availability SLO's). |
| <CopyableCode code="stringRestrictions" /> | `object` | Restrictions on STRING type values |
| <CopyableCode code="supportedDbVersions" /> | `array` | Major database engine versions for which this flag is supported. |
| <CopyableCode code="valueType" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> |
