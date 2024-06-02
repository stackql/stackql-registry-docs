---
title: instances_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_config
  - notebooks
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
<tr><td><b>Name</b></td><td><code>instances_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="notebooks.instances_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availableImages" /> | `array` | Output only. The list of available images to create a WbI. |
| <CopyableCode code="defaultValues" /> | `object` | DefaultValues represents the default configuration values. |
| <CopyableCode code="supportedValues" /> | `object` | SupportedValues represents the values supported by the configuration. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_config" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> |
