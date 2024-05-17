---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.regions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="optInStatus" /> | `string` | The Region opt-in status. The possible values are &lt;code&gt;opt-in-not-required&lt;/code&gt;, &lt;code&gt;opted-in&lt;/code&gt;, and &lt;code&gt;not-opted-in&lt;/code&gt;. |
| <CopyableCode code="regionEndpoint" /> | `string` | The Region service endpoint. |
| <CopyableCode code="regionName" /> | `string` | The name of the Region. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="regions_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
