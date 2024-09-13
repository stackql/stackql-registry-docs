---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - workloadmanager
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

Creates, updates, deletes, gets or lists a <code>rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workloadmanager.rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | rule name |
| <CopyableCode code="description" /> | `string` | descrite rule in plain language |
| <CopyableCode code="displayName" /> | `string` | the name display in UI |
| <CopyableCode code="errorMessage" /> | `string` | the message template for rule |
| <CopyableCode code="primaryCategory" /> | `string` | the primary category |
| <CopyableCode code="remediation" /> | `string` | the remediation for the rule |
| <CopyableCode code="revisionId" /> | `string` | Output only. the version of the rule |
| <CopyableCode code="secondaryCategory" /> | `string` | the secondary category |
| <CopyableCode code="severity" /> | `string` | the severity of the rule |
| <CopyableCode code="tags" /> | `array` | List of user-defined tags |
| <CopyableCode code="uri" /> | `string` | the docuement url for the rule |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists rules in a given project. |

## `SELECT` examples

Lists rules in a given project.

```sql
SELECT
name,
description,
displayName,
errorMessage,
primaryCategory,
remediation,
revisionId,
secondaryCategory,
severity,
tags,
uri
FROM google.workloadmanager.rules
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
