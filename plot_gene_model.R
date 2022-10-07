
library(stringr)


hmm.df <- read.delim("/Users/jax/Google Drive/++github/hmmer-to-table/test_files/compiled_table.txt")


head(hmm.df)


protein <- unique(hmm.df$target_accession)[3]


df <- hmm.df[hmm.df$target_accession == protein,]
head(df)

df <- df[order(df$ali_from),]
df <- df[df$dom_qual == "!",]

df$col <- rainbow(nrow(df))

df$y <- seq(nrow(df), 1, -1)

box.h = 0.1



plot(0,0,type='n', xlim=c(0, max(df$ali_to)), ylim=c(0, nrow(df)+1), xlab='', ylab='', axes=F)
abline(v=axisTicks(c(0, max(df$ali_to)), F), col=scales::alpha('red',.5), lty=3)
axis(3)

segments(0, nrow(df)+1, max(df$ali_to), nrow(df)+1, lwd=2)
rect(df$ali_from, nrow(df)+box.h+1, df$ali_to,  nrow(df)-box.h+1, col=df$col)

rect(df$ali_from, df$y+box.h, df$ali_to,  df$y-box.h, col=df$col)
text(df$ali_from, df$y, df$query, pos=2)








