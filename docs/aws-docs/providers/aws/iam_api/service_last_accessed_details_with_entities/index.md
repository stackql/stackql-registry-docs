---
title: service_last_accessed_details_with_entities
hide_title: false
hide_table_of_contents: false
keywords:
  - service_last_accessed_details_with_entities
  - iam_api
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
<tr><td><b>Name</b></td><td><code>service_last_accessed_details_with_entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam_api.service_last_accessed_details_with_entities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="EntityDetailsList" /> | `array` | An &lt;code&gt;EntityDetailsList&lt;/code&gt; object that contains details about when an IAM entity (user or role) used group or policy permissions in an attempt to access the specified Amazon Web Services service. |
| <CopyableCode code="Error" /> | `object` | &lt;p&gt;Contains information about the reason that the operation failed.&lt;/p&gt; &lt;p&gt;This data type is used as a response element in the &lt;a&gt;GetOrganizationsAccessReport&lt;/a&gt;, &lt;a&gt;GetServiceLastAccessedDetails&lt;/a&gt;, and &lt;a&gt;GetServiceLastAccessedDetailsWithEntities&lt;/a&gt; operations.&lt;/p&gt; |
| <CopyableCode code="IsTruncated" /> | `boolean` | A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the &lt;code&gt;Marker&lt;/code&gt; request parameter to retrieve more items. Note that IAM might return fewer than the &lt;code&gt;MaxItems&lt;/code&gt; number of results even when there are more results available. We recommend that you check &lt;code&gt;IsTruncated&lt;/code&gt; after every call to ensure that you receive all your results. |
| <CopyableCode code="JobCompletionDate" /> | `string` | &lt;p&gt;The date and time, in &lt;a href="http://www.iso.org/iso/iso8601"&gt;ISO 8601 date-time format&lt;/a&gt;, when the generated report job was completed or failed.&lt;/p&gt; &lt;p&gt;This field is null if the job is still in progress, as indicated by a job status value of &lt;code&gt;IN_PROGRESS&lt;/code&gt;.&lt;/p&gt; |
| <CopyableCode code="JobCreationDate" /> | `string` | The date and time, in &lt;a href="http://www.iso.org/iso/iso8601"&gt;ISO 8601 date-time format&lt;/a&gt;, when the report job was created. |
| <CopyableCode code="JobStatus" /> | `string` | The status of the job. |
| <CopyableCode code="Marker" /> | `string` | When &lt;code&gt;IsTruncated&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;, this element is present and contains the value to use for the &lt;code&gt;Marker&lt;/code&gt; parameter in a subsequent pagination request. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="service_last_accessed_details_with_entities_Get" /> | `SELECT` | <CopyableCode code="JobId, ServiceNamespace, region" /> |
