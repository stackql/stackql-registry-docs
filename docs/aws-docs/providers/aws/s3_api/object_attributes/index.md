---
title: object_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - object_attributes
  - s3_api
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
<tr><td><b>Name</b></td><td><code>object_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3_api.object_attributes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="Checksum" /> | `object` | Contains all the possible checksum or digest values for an object. |
| <CopyableCode code="ETag" /> | `string` | An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL. |
| <CopyableCode code="ObjectParts" /> | `object` | A collection of parts associated with a multipart upload. |
| <CopyableCode code="ObjectSize" /> | `integer` | The size of the object in bytes. |
| <CopyableCode code="StorageClass" /> | `string` | &lt;p&gt;Provides the storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html"&gt;Storage Classes&lt;/a&gt;.&lt;/p&gt; |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="object_attributes_Get" /> | `SELECT` | <CopyableCode code="Key, x-amz-object-attributes, bucket, region" /> |
