---
title: nlp
hide_title: false
hide_table_of_contents: false
keywords:
  - nlp
  - healthcare
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

Creates, updates, deletes, gets or lists a <code>nlp</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nlp</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.nlp" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="analyze_entities" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Analyze heathcare entity in a document. Its response includes the recognized entity mentions and the relationships between them. AnalyzeEntities uses context aware models to detect entities. |
