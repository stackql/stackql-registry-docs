---
title: key_pairs
hide_title: false
hide_table_of_contents: false
keywords:
  - key_pairs
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
<tr><td><b>Name</b></td><td><code>key_pairs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.key_pairs" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="key_pairs_Describe" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Describes the specified key pairs or all of your key pairs.&lt;/p&gt; &lt;p&gt;For more information about key pairs, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html"&gt;Amazon EC2 key pairs&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="key_pair_Create" /> | `INSERT` | <CopyableCode code="KeyName, region" /> | &lt;p&gt;Creates an ED25519 or 2048-bit RSA key pair with the specified name and in the specified PEM or PPK format. Amazon EC2 stores the public key and displays the private key for you to save to a file. The private key is returned as an unencrypted PEM encoded PKCS#1 private key or an unencrypted PPK formatted private key for use with PuTTY. If a key with the specified name already exists, Amazon EC2 returns an error.&lt;/p&gt; &lt;p&gt;The key pair returned to you is available only in the Amazon Web Services Region in which you create it. If you prefer, you can create your own key pair using a third-party tool and upload it to any Region using &lt;a&gt;ImportKeyPair&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can have up to 5,000 key pairs per Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html"&gt;Amazon EC2 key pairs&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="key_pair_Delete" /> | `DELETE` | <CopyableCode code="region" /> | Deletes the specified key pair, by removing the public key from Amazon EC2. |
| <CopyableCode code="key_pair_Import" /> | `EXEC` | <CopyableCode code="KeyName, PublicKeyMaterial, region" /> | &lt;p&gt;Imports the public key from an RSA or ED25519 key pair that you created with a third-party tool. Compare this with &lt;a&gt;CreateKeyPair&lt;/a&gt;, in which Amazon Web Services creates the key pair and gives the keys to you (Amazon Web Services keeps a copy of the public key). With ImportKeyPair, you create the key pair and give Amazon Web Services just the public key. The private key is never transferred between you and Amazon Web Services.&lt;/p&gt; &lt;p&gt;For more information about key pairs, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html"&gt;Amazon EC2 key pairs&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
