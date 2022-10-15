type Ham<L, T extends any[] = []> =  T extends { length: L } ? T : Ham<L, [...T, any]>;
type Spam<A, B> = A extends any[] ? B extends any[] ? [...A, ...B] : never : never;
type Sham<A, B> = A extends any[] ? B extends any[] ? A extends [...infer U, ...B] ? U : never : never : never;

declare const Damn: unique symbol;
declare const Cram: unique symbol;
declare const Flam: unique symbol;
declare const Glam: unique symbol;
declare const Dam: unique symbol;
declare const Can: unique symbol;

type Damn = typeof Damn;
type Cram = typeof Cram;
type Flam = typeof Flam;
type Glam = typeof Glam;
type Dam = typeof Dam;

type Lan<A, B> = [A, B];
type Can = typeof Can;

type Go<X, Y extends any[] = []> =
  X extends Lan<[Damn, infer E], infer N> ? Go<N, [Ham<E>, ...Y]> :
  X extends Lan<[Cram], infer N> ?
    Y extends [infer A, infer B, ...infer R] ? Go<N, [Spam<B, A>, ...R]> : never :
  X extends Lan<[Glam], infer N> ?
    Y extends [infer A, infer B, ...infer R] ? Go<N, [Sham<B, A>, ...R]> : never :
  X extends Lan<[Dam], infer N> ? true :
  X extends Lan<[Flam, infer A, infer B], Can> ?
    Y extends [infer H, ...infer R] ? 
      H extends [] ? Go<A, R> : Go<B, R>
      : never :
  never;

type Suffer = Lan<[Damn, Flag00], Lan<[Damn, 15], Lan<[Cram], Lan<[Damn, 25], Lan<[Cram], Lan<[Damn, 25], Lan<[Cram], Lan<[Damn, 87], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag01], Lan<[Damn, 21], Lan<[Cram], Lan<[Damn, 19], Lan<[Cram], Lan<[Damn, 11], Lan<[Cram], Lan<[Damn, 58], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag02], Lan<[Damn, 18], Lan<[Cram], Lan<[Damn, 22], Lan<[Cram], Lan<[Damn, 24], Lan<[Cram], Lan<[Damn, 90], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag03], Lan<[Damn, 13], Lan<[Cram], Lan<[Damn, 18], Lan<[Cram], Lan<[Damn, 12], Lan<[Cram], Lan<[Damn, 79], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag04], Lan<[Damn, 27], Lan<[Cram], Lan<[Damn, 18], Lan<[Cram], Lan<[Damn, 16], Lan<[Cram], Lan<[Damn, 74], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag05], Lan<[Damn, 14], Lan<[Cram], Lan<[Damn, 10], Lan<[Cram], Lan<[Damn, 21], Lan<[Cram], Lan<[Damn, 74], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag06], Lan<[Damn, 11], Lan<[Cram], Lan<[Damn, 23], Lan<[Cram], Lan<[Damn, 20], Lan<[Cram], Lan<[Damn, 83], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag07], Lan<[Damn, 13], Lan<[Cram], Lan<[Damn, 24], Lan<[Cram], Lan<[Damn, 13], Lan<[Cram], Lan<[Damn, 53], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag08], Lan<[Damn, 26], Lan<[Cram], Lan<[Damn, 21], Lan<[Cram], Lan<[Damn, 18], Lan<[Cram], Lan<[Damn, 83], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag09], Lan<[Damn, 10], Lan<[Cram], Lan<[Damn, 27], Lan<[Cram], Lan<[Damn, 22], Lan<[Cram], Lan<[Damn, 95], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag10], Lan<[Damn, 22], Lan<[Cram], Lan<[Damn, 23], Lan<[Cram], Lan<[Damn, 11], Lan<[Cram], Lan<[Damn, 86], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag11], Lan<[Damn, 18], Lan<[Cram], Lan<[Damn, 29], Lan<[Cram], Lan<[Damn, 22], Lan<[Cram], Lan<[Damn, 105], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag12], Lan<[Damn, 18],  Lan<[Cram], Lan<[Damn, 25], Lan<[Cram], Lan<[Damn, 28], Lan<[Cram], Lan<[Damn, 80], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag13], Lan<[Damn, 24], Lan<[Cram], Lan<[Damn, 21], Lan<[Cram], Lan<[Damn, 21], Lan<[Cram], Lan<[Damn, 84], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag14], Lan<[Damn, 21], Lan<[Cram], Lan<[Damn, 10], Lan<[Cram], Lan<[Damn, 10], Lan<[Cram], Lan<[Damn, 77], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag15], Lan<[Damn, 11], Lan<[Cram], Lan<[Damn, 23], Lan<[Cram], Lan<[Damn, 20], Lan<[Cram], Lan<[Damn, 71], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag16], Lan<[Damn, 20], Lan<[Cram], Lan<[Damn, 23], Lan<[Cram], Lan<[Damn, 16], Lan<[Cram], Lan<[Damn, 79], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag17], Lan<[Damn, 24], Lan<[Cram], Lan<[Damn, 19], Lan<[Cram], Lan<[Damn, 26], Lan<[Cram], Lan<[Damn, 82], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag18], Lan<[Damn, 13], Lan<[Cram], Lan<[Damn, 27], Lan<[Cram], Lan<[Damn, 25], Lan<[Cram], Lan<[Damn, 84], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag19], Lan<[Damn, 12], Lan<[Cram], Lan<[Damn, 17], Lan<[Cram], Lan<[Damn, 23], Lan<[Cram], Lan<[Damn, 79], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag20], Lan<[Damn, 15], Lan<[Cram], Lan<[Damn, 19], Lan<[Cram], Lan<[Damn, 13], Lan<[Cram], Lan<[Damn, 59], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag21], Lan<[Damn, 15], Lan<[Cram], Lan<[Damn, 18], Lan<[Cram], Lan<[Damn, 13], Lan<[Cram], Lan<[Damn, 75], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag22], Lan<[Damn, 22], Lan<[Cram], Lan<[Damn, 29], Lan<[Cram], Lan<[Damn, 10], Lan<[Cram], Lan<[Damn, 97], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag23], Lan<[Damn, 28], Lan<[Cram], Lan<[Damn, 25], Lan<[Cram], Lan<[Damn, 13], Lan<[Cram], Lan<[Damn, 88], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag24], Lan<[Damn, 29], Lan<[Cram], Lan<[Damn, 24], Lan<[Cram], Lan<[Damn, 23], Lan<[Cram], Lan<[Damn, 83], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag25], Lan<[Damn, 15], Lan<[Cram], Lan<[Damn, 19], Lan<[Cram], Lan<[Damn, 10], Lan<[Cram], Lan<[Damn, 73], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag26], Lan<[Damn, 20], Lan<[Cram], Lan<[Damn, 21], Lan<[Cram], Lan<[Damn, 11], Lan<[Cram], Lan<[Damn, 65], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag27], Lan<[Damn, 24], Lan<[Cram], Lan<[Damn, 16], Lan<[Cram], Lan<[Damn, 25], Lan<[Cram], Lan<[Damn, 101], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag28], Lan<[Damn, 14], Lan<[Cram], Lan<[Damn, 19], Lan<[Cram], Lan<[Damn, 28], Lan<[Cram], Lan<[Damn, 81], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag29], Lan<[Damn, 11], Lan<[Cram], Lan<[Damn, 25], Lan<[Cram], Lan<[Damn, 16], Lan<[Cram], Lan<[Damn, 88], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag30], Lan<[Damn, 16], Lan<[Cram], Lan<[Damn, 27], Lan<[Cram], Lan<[Damn, 16], Lan<[Cram], Lan<[Damn, 66], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag31], Lan<[Damn, 22], Lan<[Cram], Lan<[Damn, 27], Lan<[Cram], Lan<[Damn, 23], Lan<[Cram], Lan<[Damn, 102], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag32], Lan<[Damn, 14], Lan<[Cram], Lan<[Damn, 10], Lan<[Cram], Lan<[Damn, 19], Lan<[Cram], Lan<[Damn, 64], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag33], Lan<[Damn, 24], Lan<[Cram], Lan<[Damn, 12], Lan<[Cram], Lan<[Damn, 12], Lan<[Cram], Lan<[Damn, 77], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag34], Lan<[Damn, 15], Lan<[Cram], Lan<[Damn, 11], Lan<[Cram], Lan<[Damn, 24], Lan<[Cram], Lan<[Damn, 86], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag35], Lan<[Damn, 12], Lan<[Cram], Lan<[Damn, 22], Lan<[Cram], Lan<[Damn, 23], Lan<[Cram], Lan<[Damn, 76], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag36], Lan<[Damn, 13], Lan<[Cram], Lan<[Damn, 10], Lan<[Cram], Lan<[Damn, 26], Lan<[Cram], Lan<[Damn, 73], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag37], Lan<[Damn, 29], Lan<[Cram], Lan<[Damn, 15], Lan<[Cram], Lan<[Damn, 23], Lan<[Cram], Lan<[Damn, 82], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag38], Lan<[Damn, 26], Lan<[Cram], Lan<[Damn, 20], Lan<[Cram], Lan<[Damn, 26], Lan<[Cram], Lan<[Damn, 101], Lan<[Glam], Lan<[Flam, Lan<[Damn, Flag39], Lan<[Damn, 22], Lan<[Cram], Lan<[Damn, 28], Lan<[Cram], Lan<[Damn, 25], Lan<[Cram], Lan<[Damn, 93], Lan<[Glam], Lan<[Flam, Lan<[Dam], Can>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>, Can], Can>>>>>>>>>>;

// alphabet: "abcdefghijklmnopqrstuvwxyz0123456789_"
type Ord<R extends keyof Lookup> = Lookup[R];
type Chr<L extends keyof LookupInv> = LookupInv[L];
type Join<T extends (keyof LookupInv)[]> =
  T extends [] ? "" :
  T extends [infer H, ...infer T] ?
    H extends keyof LookupInv ?
    T extends (keyof LookupInv)[] ? `${Chr<H>}${Join<T>}` : never : never : never;
type Lookup = {"0":26,"1":27,"2":28,"3":29,"4":30,"5":31,"6":32,"7":33,"8":34,"9":35,"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,"_":36};
type LookupInv = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z",26:"0",27:"1",28:"2",29:"3",30:"4",31:"5",32:"6",33:"7",34:"8",35:"9",36:"_"};

type Flag = `TUDCTF{${Join<[Flag00, Flag01, Flag02, Flag03, Flag04, Flag05, Flag06, Flag07, Flag08, Flag09, Flag10, Flag11, Flag12, Flag13, Flag14, Flag15, Flag16, Flag17, Flag18, Flag19, Flag20, Flag21, Flag22, Flag23, Flag24, Flag25, Flag26, Flag27, Flag28, Flag29, Flag30, Flag31, Flag32, Flag33, Flag34, Flag35, Flag36, Flag37, Flag38, Flag39]>}}`;

// Adjust the following lines...
type Flag00 = Ord<'a'>;
type Flag01 = Ord<'a'>;
type Flag02 = Ord<'a'>;
type Flag03 = Ord<'a'>;
type Flag04 = Ord<'a'>;
type Flag05 = Ord<'a'>;
type Flag06 = Ord<'a'>;
type Flag07 = Ord<'a'>;
type Flag08 = Ord<'a'>;
type Flag09 = Ord<'a'>;
type Flag10 = Ord<'a'>;
type Flag11 = Ord<'a'>;
type Flag12 = Ord<'a'>;
type Flag13 = Ord<'a'>;
type Flag14 = Ord<'a'>;
type Flag15 = Ord<'a'>;
type Flag16 = Ord<'a'>;
type Flag17 = Ord<'a'>;
type Flag18 = Ord<'a'>;
type Flag19 = Ord<'a'>;
type Flag20 = Ord<'a'>;
type Flag21 = Ord<'a'>;
type Flag22 = Ord<'a'>;
type Flag23 = Ord<'a'>;
type Flag24 = Ord<'a'>;
type Flag25 = Ord<'a'>;
type Flag26 = Ord<'a'>;
type Flag27 = Ord<'a'>;
type Flag28 = Ord<'a'>;
type Flag29 = Ord<'a'>;
type Flag30 = Ord<'a'>;
type Flag31 = Ord<'a'>;
type Flag32 = Ord<'a'>;
type Flag33 = Ord<'a'>;
type Flag34 = Ord<'a'>;
type Flag35 = Ord<'a'>;
type Flag36 = Ord<'a'>;
type Flag37 = Ord<'a'>;
type Flag38 = Ord<'a'>;
type Flag39 = Ord<'a'>;

// to make this line compile
const make_this_line_compile: Go<Suffer> = true;

// once the previous line compiles, hover over "flag" to see the flag
let flag: Flag;